for page in range(0, number_of_pages):
    result = client['my_db']['videos_data'].aggregate([
        {
            '$match': {
                'country': {
                    '$in': [
                        'US', 'GB'
                    ]
                }
            }
        }, 
        {
            '$unwind': {
                'path': '$tags'
            }
        }, 
        {
            '$group': {
                '_id': '$tags', 
                'tag': {
                    '$first': '$tags'
                }, 'count': {
'$sum': 1
}
}
},
{
'$sort': {
'count': -1
}
},
{
'$project': {
'tag': 1,
'count': 1,
'_id': 0
}
},
{
'$limit': page_size
},
{
'$skip': page * page_size
}
])