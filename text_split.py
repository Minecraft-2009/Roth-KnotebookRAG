from split import split_text
from embed_and_store import add_documents


test_text = """
Earendil was a mariner who tarried in Arvenien
He built a boat of timer felled in Nimbrethel to journey in
Her sails he wove of silver fair of silver were her lanterns made
Her prow was fashioned like a swan and light upon her banners laid
In panoply of Ancient kings in chained rings he armoured him
His shining shield was scored with runes to ward all runes and harm from him
His sword of steel was valiant of adamant his helmet tall
An eagle plume upon his crest upon his breast an emerald
Beneath the moon and under star he wandered far on northern strands
Bewildered on enchanted ways beyond the days of mortal lands
From gnashing of the narrow ice where shadow lies on frozen hills
From nether heats and burning waste he turned in haste and roving still
On starless waters far a stray at last he came ti night of naught
And passed and never sight he saw of shining shore nor light he sought
The winds of wrath came driving him and blindly in the foam he fled
From east to west and errandless unheralded he homeward sped
"""


user_id = '321'
document_id = '12345'
splits = split_text(test_text, user_id, document_id)
for split in splits:
    print(split.page_content[:50], split.metadata)

vector_ids = add_documents(splits)
print('---------------')
print(vector_ids)