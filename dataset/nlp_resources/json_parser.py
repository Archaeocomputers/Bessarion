import argparse
import json
from colorama import Fore, Style


class Inscription():
    def __init__(self, json_inscription):
        self.image_filename = json_inscription['filename'] #TODO: This should be a list of filenames pointing to the same inscription
        try:
            self.gt_text = json_inscription['text']
        except:
            self.gt_text = ''

    def __str__(self):
        string = f'Αρχείο εικόνας: {self.image_filename} \n'
        #string += show_image(self.image_filename)
        string += f'Κείμενο στην επιγραφή: {self.gt_text}'
        return(string)

class BessarionSite():
    def __init__(self, json_site):
        self.site_id = int(json_site['site_id'])
        self.name = json_site['name']
        self.village = json_site['village']
        self.founder = json_site['founder']
        self.date = json_site['date']
        try:
            self.date_intext = json_site['date_intext']
        except:
            self.date_intext = ''
        try:
            self.founder_intext = json_site['founder_intext']
        except:
            self.founder_intext = ''
        try:
            self.date_type = json_site['date_type']
        except:
            self.date_type = ''
        try:
            self.founder_intext_extended = json_site['founder_intext_extended']
        except:
            self.founder_intext_extended = ''
        try:
            self.year_words = json_site['year_words']
        except:
            self.year_words = ''
        try:
            self.month_words = json_site['month_words']
        except:
            self.month_words = ''
        try:
            self.name_words = json_site['name_words']
        except:
            self.name_words = ''            
        try:
            self.comment = json_site['comment']
        except:
            self.comment = ''
        #
        self.inscriptions = []
        for i in json_site['inscriptions']:
            self.inscriptions.append(Inscription(i))


    def c(self, string):
        return(Fore.BLUE + string + Style.RESET_ALL)
    
    def __str__(self):
        string = ''
        string += f'** {self.c(self.name)} (site id: {self.c(str(self.site_id))}) ** \n'
        string += f'Βρίσκεται στη θέση: {self.c(self.village)}\n'
        string += f'Το όνομα του κτίτορα είναι: {self.c(self.founder)}\n'
        string += f'Στην επιγραφή ο κτίτορας υποδεικνύεται με τις λέξεις: {self.c(self.founder_intext_extended)}\n'
        string += f'Στην επιγραφή, πιο συγκεκριμένα τα σχετικά ονόματα είναι: {self.c(self.founder_intext)}\n'
        string += f'Η χρονολογία που οικοδομήθηκε ο ναός είναι: {self.c(self.date)}\n'
        string += f'Στην επιγραφή η χρονολογία υποδεικνύεται με τις λέξεις ή αριθμό: {self.c(self.date_intext)}\n'
        string += f'Στην επιγραφή το έτος υποδεικνύεται με την λέξη ή αριθμό: {self.c(self.year_words)}\n'
        string += f'Στην επιγραφή ο μήνας υποδεικνύεται με την λέξη: {self.c(self.month_words)}\n'
        string += f'Στην επιγραφή κύρια ονόματα (όχι απαραίτητα κτίτορες) υποδεικνύονται με τις λέξεις: {self.c(self.name_words)}\n'
        if self.comment != '':
            string += self.c(self.comment)
        string += f'Στην βάση δεδομένων έχουμε {self.c(str(len(self.inscriptions)))} επιγραφή/ές σε αυτή τη θέση.\n'
        for idx, inscription in enumerate(self.inscriptions):
            string += f'Επιγραφή {idx+1} -- {inscription}\n'
        return(string)


#def print_summary(site):
#    equalsigns = 150
#    print('='*equalsigns)
#    print(site)
#    #print('='*equalsigns)


if __name__=='__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--jsonfile', required=False, default='ktitorikes.json')
    parser.add_argument('--summary', dest='summary', action='store_true', help='Print summary for all data.')
    parser.add_argument('--id', type=int, default=-1, help='Specify id of the site we are interested in.')    
    args = parser.parse_args()
    print('###########################################')
    print('Experiment Parameters:')
    for key, value in vars(args).items():
        print(f'{str(key)}: {str(value)}')
    print('###########################################')


    with open(args.jsonfile) as f:
        allsites = json.load(f)

    print(f'Το αρχείο {args.jsonfile} περιέχει {len(allsites)} εγγραφές.')

    for site in allsites:
        bs = BessarionSite(site)
        if(args.summary or args.id == bs.site_id):
            print(bs)
