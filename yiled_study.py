# def fool():
#     print("fool1111")
#     yield print("fool2222")
#     print("fool3333")
#     yield {
#         'foo': 'bar',
#         'bar': 'baz'
#     }
#
# def fool2():
#     print("2fool1111")
#     print("2fool2222")
#     yield print("2fool3333")
# f=fool()
# print("*"*20)
# next(f)
# print("*"*20)
# x=next(f)
# print(x)
# print("*"*20)
# next(fool2())
#
# # ********************
# # fool1111
# # fool2222
# # ********************
# # fool3333
# # {'foo': 'bar', 'bar': 'baz'}
# # ********************
# # 2fool1111
# # 2fool2222
# # 2fool3333

def fool():
    for i in range(10):
        yield print(i)

f=fool()
next(f)
next(f)


# 0
# 1