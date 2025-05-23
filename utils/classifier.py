import torch
from speechbrain.inference.classifiers  import EncoderClassifier

classifier = EncoderClassifier.from_hparams(source="Jzuluaga/accent-id-commonaccent_ecapa", savedir="pretrained_models/accent-id-commonaccent_ecapa")

country_dict = {
    "US": "American",
    "GB": "British",
    "AU": "Australian",
    "IN": "Indian",
    "CA": "Canadian",
    "NG": "Nigerian",
    "ZA": "South African",
    "IE": "Irish",
    "NZ": "New Zealander",
    "PH": "Filipino",
    "SG": "Singaporean",
    "KE": "Kenyan",
    "GH": "Ghanaian"
}


def detect_accent(file_path: str):
    _, score, _, country_code = classifier.classify_file(file_path)
    score, text_lab = torch.tensor(score).item(), country_code[0]
    percent_score, country_code = score * 100, text_lab.upper()
    if country_code in country_dict:
        country_code = country_dict[country_code]
    else:
        country_code = "Unknown"
    return percent_score, country_code
