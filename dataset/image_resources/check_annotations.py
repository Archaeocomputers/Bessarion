import sys,os
import logging,argparse

logger = logging.getLogger('Check_datasets')
logger.info('--- Check BESSARION annotations ---')
#logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
# argument parsing
parser = argparse.ArgumentParser()
# - train arguments
parser.add_argument('--dataset_folder', required=False, #type=argparse.FileType('rb'),
                    default='.',
                    help='Root folder containing datasets.')
args = parser.parse_args()

logger.info('###########################################')
logger.info('######## Experiment Parameters ############')
for key, value in vars(args).items():
    logger.info('%s: %s', str(key), str(value))
logger.info('###########################################')

args.dataset = args.dataset_folder
images_dataset = '{}/'.format(args.dataset)
annotations_dataset = '{}/'.format(args.dataset_folder)


print(images_dataset, annotations_dataset)

#
matching_pair = 0
missing_pair = 0
backup_pair = 0
#
for root, dirs, files in os.walk(annotations_dataset):
    for file in files:
        if file.endswith(".xml"):
            image_exists = False
            a = root.split('/')
            a = a[1:]
            a.insert(0, args.dataset)
            #a.insert(0, '..')
            b = os.path.join('', *a)
            filename, extension = os.path.splitext(file)
            for imgext in ['jpg', 'jpeg', 'tiff','JPG']:
                if image_exists is True:
                    break
                c = '{}/{}.{}'.format(b, filename, imgext)
                if(os.path.isfile(c)):
                    matching_pair += 1
                    image_exists = True
            if('~' in c):
                backup_pair += 1
            elif(image_exists is False):
                print('WARNING! No image found for..{}'.format(root+'/'+file))
                missing_pair += 1

print('Found {} pairs of xml+image files under folder "{}".'.format(matching_pair, args.dataset_folder))
print('Failed to find a pair in {} instances.'.format(missing_pair))