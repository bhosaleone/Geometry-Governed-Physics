import zipfile
import xml.etree.ElementTree as ET
import sys

def extract_docx_text(docx_path):
    try:
        with zipfile.ZipFile(docx_path, 'r') as zip_ref:
            xml_content = zip_ref.read('word/document.xml')
            tree = ET.fromstring(xml_content)
            
            # Namespaces for Word XML
            ns = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
            
            text_elements = tree.findall('.//w:t', ns)
            text = ''.join([el.text for el in text_elements if el.text])
            return text
    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python extract_docx_text.py <path_to_docx>")
        sys.exit(1)
    
    # Use utf-8 for output
    sys.stdout.reconfigure(encoding='utf-8')
    
    docx_path = sys.argv[1]
    print(extract_docx_text(docx_path))
