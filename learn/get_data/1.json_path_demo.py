from jsonpath import jsonpath

data = {'key1': {'key2': {'key3': {'key4': {'key5': {'key6': 'python'}}}}}}

print(data['key1']['key2']['key3']['key4']['key5']['key6'])

# 索引
print(jsonpath(data, '$.key1.key2.key3.key4.key5.key6')[0])
# 非索引
print(jsonpath(data, '$..key6')[0])
