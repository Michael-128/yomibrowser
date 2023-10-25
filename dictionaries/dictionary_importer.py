from zipfile import ZipFile
import json

from .models import Dictionary, Term


def tag_bank_filter(file):
    if not "tag_bank" in file:
        return False
    return True


def term_bank_filter(file):
    if not "term_bank" in file:
        return False
    return True


def load_dictionary(dict_zip):
    with ZipFile(dict_zip) as dictionary:
        files = dictionary.namelist()
        tag_bank_files = tuple(filter(tag_bank_filter, files))
        term_bank_files = tuple(filter(term_bank_filter, files))
        
        if not "index.json" in files: raise FileNotFoundError("Index")
        if len(term_bank_files) < 1: raise FileNotFoundError("Term Bank")
        
        index = json.loads(dictionary.read("index.json"))
        
        tag_banks = list()
        for tag_bank in tag_bank_files:
            tag_banks.extend(json.loads(dictionary.read(tag_bank)))

        term_banks = list()
        for term_bank in term_bank_files:
            term_banks.extend(json.loads(dictionary.read(term_bank)))

        return {
            "index": index,
            "tag_bank": tag_banks,
            "term_bank": term_banks
        }


def import_dictionary(dict_zip):
    dictionary = load_dictionary(dict_zip)

    dictionaryEntry = Dictionary(**dictionary["index"])
    dictionaryEntry.save()

    termEntries = list()
    for term in dictionary["term_bank"]:
        term[2] = term[2] + " " + term[-1]
        term[-1] = dictionaryEntry
        
        termEntry = Term(
            term = term[0],
            reading = term[1],
            tags = term[2],
            ruleIdentifiers = term[3],
            popularity = term[4],
            definitions = json.dumps(term[5]),
            sequence = term[6],
            dictionary = term[7]
        )
        termEntries.append(termEntry)

    Term.objects.bulk_create(termEntries)
    # Create new dictionary if it doesn't exist
    # Create new tags
    # Create new terms


