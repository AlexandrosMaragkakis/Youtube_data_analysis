from pymongo import MongoClient
import matplotlib.pyplot as plt
import numpy as np

# Requires the PyMongo package.
# https://api.mongodb.com/python/current

client = MongoClient('mongodb://localhost:27017/')
result1 = client['my_db']['videos_data'].aggregate([
    {
        '$match': {
            'country': 'GB', 
            'comments_disabled': True
        }
    }, {
        '$group': {
            '_id': None, 
            'avg_views': {
                '$avg': '$view_count'
            }, 
            'avg_likes': {
                '$avg': '$likes'
            }, 
            'avg_dislikes': {
                '$avg': '$dislikes'
            }
        }
    }, {
        '$project': {
            '_id': 0, 
            'avg_views': {
                '$trunc': [
                    '$avg_views', 2
                ]
            }, 
            'avg_likes': {
                '$trunc': [
                    '$avg_likes', 2
                ]
            }, 
            'avg_dislikes': {
                '$trunc': [
                    '$avg_dislikes', 2
                ]
            }
        }
    }
])


result2 = client['my_db']['videos_data'].aggregate([
    {
        '$match': {
            'country': 'GB', 
            'comments_disabled': False
        }
    }, {
        '$group': {
            '_id': None, 
            'avg_views': {
                '$avg': '$view_count'
            }, 
            'avg_likes': {
                '$avg': '$likes'
            }, 
            'avg_dislikes': {
                '$avg': '$dislikes'
            }
        }
    }, {
        '$project': {
            '_id': 0, 
            'avg_views': {
                '$trunc': [
                    '$avg_views', 2
                ]
            }, 
            'avg_likes': {
                '$trunc': [
                    '$avg_likes', 2
                ]
            }, 
            'avg_dislikes': {
                '$trunc': [
                    '$avg_dislikes', 2
                ]
            }
        }
    }
])

avg_views = []
avg_likes = []
avg_dislikes = []

comments_disabled = []
comments_enabled = []

for item in result1:
    comments_disabled.append(item['avg_views'])
    comments_disabled.append(item['avg_likes'])
    comments_disabled.append(item['avg_dislikes'])

for item in result2:
    comments_enabled.append(item['avg_views'])
    comments_enabled.append(item['avg_likes'])
    comments_enabled.append(item['avg_dislikes'])


labels = ['avg_views', 'avg_likes', 'avg_dislikes']
x = np.arange(len(labels))
width = 0.15

fig, ax = plt.subplots()
rects1 = ax.bar(x + 0.00, comments_enabled, width, label='comments_enabled')
rects2 = ax.bar(x + 0.35, comments_disabled, width, label='comments_disabled')


ax.set_xticks(x, labels)
ax.legend()

ax.bar_label(rects1, padding=5)
ax.bar_label(rects2, padding=5)

fig.tight_layout()

plt.show()