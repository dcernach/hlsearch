import xml.etree.ElementTree as ET
import os
import re
import zipfile
import string


class HeroLab:

    def __init__(self):
        pass


class HeroLabIndex:

    def __init__(self, search_folder):
        self.search_folder = search_folder

    def get_creatures(self):

        self.bad_files = []
       # Parse Por/Stock files
        for filename in os.listdir(self.search_folder):
            if re.match('.*\.stock|.*\.por', filename):
                try:
                    lab_zip = zipfile.ZipFile(str(self.search_folder) + '/' + filename, 'r')
                    index_xml = lab_zip.open('index.xml')
                    tree = ET.parse(index_xml)
                    index_xml.close()
                    index_root = tree.getroot()
                    for index_char in index_root.find('characters').iter('character'):
                        name = index_char.get('name')
                        summary = index_char.get('summary')
                        found = re.search(' CR (\d+/?\d*)$', summary)
                        cr = found.group(1)
                        yield {"name": name, "summary": summary, "cr": cr, "filename": filename}

                    lab_zip.close()
                except zipfile.BadZipfile:
                    self.bad_files.append(filename)
