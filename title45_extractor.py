import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import time
import os

def get_title45_pdf_links():
    """
    Scrape all PDF links for Title 45 from ND Administrative Code
    """
    base_url = "https://ndlegis.gov/information/acdata/"
    title45_url = "https://ndlegis.gov/information/acdata/html/title45.html"
    
    # Store all PDF links
    pdf_links = []
    
    print("Fetching Title 45 page...")
    response = requests.get(title45_url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find all article links
    article_links = soup.find_all('a', href=True)
    
    print(f"Found {len(article_links)} links on Title 45 page\n")
    
    for link in article_links:
        href = link.get('href')
        
        # Check if it's an article/chapter page (HTML)
        #Only visit links that are HTML pages and part of Title 45
        if href.endswith('.html') and '45-' in href:
            #Visit the article page to find chapter PDFs
            article_url = urljoin(base_url + 'html/', href) # This resolves correctly
            print(f"Checking article page: {article_url}")
                       
            try:
                article_response = requests.get(article_url)
                article_response.raise_for_status() # Check for 4xx/5xx errors
                article_soup = BeautifulSoup(article_response.content, 'html.parser')
                
                # Find PDF links on this article page
                article_pdf_links = article_soup.find_all('a', href=True)
                for pdf_link in article_pdf_links:
                    pdf_href = pdf_link.get('href')
                    if pdf_href.endswith('.pdf'):
                        full_pdf_url = urljoin(base_url, pdf_href)
                        
                        pdf_links.append({
                            'url': full_pdf_url,
                            'title': pdf_link.get_text(strip=True),
                            'filename': os.path.basename(full_pdf_url)
                        })
                
                # Be polite to the server
                time.sleep(0.5)
            except requests.exceptions.RequestException as e: # Be more specific
                print(f"Error fetching {article_url}: {e}")
    
    return pdf_links

def save_links_to_file(pdf_links, filename='title45_pdf_links.txt'):
    """
    Save PDF links to a text file
    """
    with open(filename, 'w') as f:
        f.write(f"Total PDFs found: {len(pdf_links)}\n")
        f.write("="*80 + "\n\n")
        
        for i, link in enumerate(pdf_links, 1):
            f.write(f"{i}. {link['title']}\n")
            f.write(f"   Filename: {link['filename']}\n")
            f.write(f"   URL: {link['url']}\n\n")
    
    print(f"\nLinks saved to {filename}")

def download_pdfs(pdf_links, output_dir='title45_pdfs'):
    """
    Download all PDFs to a specified directory
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    print(f"\nDownloading {len(pdf_links)} PDFs to {output_dir}/\n")
    
    for i, link in enumerate(pdf_links, 1):
        try:
            print(f"[{i}/{len(pdf_links)}] Downloading {link['filename']}...")
            response = requests.get(link['url'])
            
            if response.status_code == 200:
                filepath = os.path.join(output_dir, link['filename'])
                with open(filepath, 'wb') as f:
                    f.write(response.content)
                print(f"  ✓ Saved to {filepath}")
            else:
                print(f"  ✗ Failed (Status {response.status_code})")
            
            # Be polite to the server
            time.sleep(1)
        except Exception as e:
            print(f"  ✗ Error: {e}")
    
    print(f"\nDownload complete!")

if __name__ == "__main__":
    print("North Dakota Administrative Code - Title 45 PDF Extractor")
    print("="*60)
    
    # Get all PDF links
    pdf_links = get_title45_pdf_links()
    
    # Remove duplicates
    unique_links = []
    seen_urls = set()
    for link in pdf_links:
        if link['url'] not in seen_urls:
            unique_links.append(link)
            seen_urls.add(link['url'])
    
    print(f"\n{'='*60}")
    print(f"Found {len(unique_links)} unique PDF files for Title 45")
    print(f"{'='*60}\n")
    
    # Save links to file
    save_links_to_file(unique_links)
    
    # Ask user if they want to download
    choice = input("\nDo you want to download all PDFs? (y/n): ")
    if choice.lower() == 'y':
        download_pdfs(unique_links)
    else:
        print("\nPDF links saved to file. You can use them for manual download or with other tools.")
