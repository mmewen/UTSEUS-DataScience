# #!/usr/bin/python
# # -*- coding: utf-8 -*-

# import json
# import re

# data = []
# dataCleaned = []

# reLowerUpper = re.compile("(?[a-z])(?[A-Z])")

# with open('./GOT/Game of Thrones/data/charactersNormalize.json', 'rb') as jsonfile:
# 	data = json.loads(jsonfile.read())
# 	for d in data:
#         d = reLowerUpper.sub(r"\1¤\2", d)
#         d = d.Split("¤")



# with open('./GOT/Game of Thrones/data/charactersNormalize2.json', 'wb') as f:
# 	f.write(json.dumps(data))


# print(data)

