import os
import glob
import pandas as pd
import xml.etree.ElementTree as ET


def xml_to_csv(path):
    xml_list = []
    for x_file in os.listdir(path + '/xml'):
        xml_file = path + '/xml/' + x_file
        tree = ET.parse(xml_file)
        root = tree.getroot()
        for member in root.findall('object'):
            value = (root.find('filename').text,
                     int(root.find('size')[0].text),
                     int(root.find('size')[1].text),
                     member[-1].text,
                     int(member[0][0].text),
                     int(member[0][1].text),
                     int(member[0][2].text),
                     int(member[0][3].text)
                     )
            xml_list.append(value)
    column_name = ['filename', 'width', 'height', 'class', 'xmin', 'ymin', 'xmax', 'ymax']
    xml_df = pd.DataFrame(xml_list, columns=column_name)
    return xml_df


def main():
    for folder in ['train','test']:
        image_path = os.path.join('/home/elebouder/Data/landsat', ('ssd_split/' + folder))
        xml_df = xml_to_csv(image_path)
        xml_df.to_csv(('/home/elebouder/repos/models/research/object_detection/' + folder + '_labels.csv'), index=None)
        print('Successfully converted xml to csv.')


main()
