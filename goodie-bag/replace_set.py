# coding: utf-8


def replace_set(text, dictionary):
    """ Ersätter en uppsättning tecken eller strängar med en annan.
    """
    import re

    rep = dict((re.escape(k), v) for k, v in dictionary.iteritems())
    pattern = re.compile("|".join(rep.keys()))
    return pattern.sub(lambda m: rep[re.escape(m.group(0))], text)


text = replace_set("åbäke", {'å': 'a',
                             'ä': 'a',
                             'ö': 'o'
                             })
print(text)


text = replace_set("coka cola", {'cola': 'coka',
                                 'coka': 'cola'})
print(text)


text = replace_set("sju sjösjuka sjömän", {'sj': 'ʃ'})
print(text)
