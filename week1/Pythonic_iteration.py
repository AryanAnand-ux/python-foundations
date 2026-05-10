results = [{'loss': 0.5, 'epoch': 1}, {'loss': 0.2, 'epoch': 2}, {'loss': 0.15, 'epoch': 3}]

po = [x['loss'] for x in results if x['loss'] <0.3 ]
print(po)

def batch_generator(data, batch_size):
    for i in range(0, len(data), batch_size):
        yield data[i:i+ batch_size]

li = [( 'model_A', 0.92), ('model_B', 0.95), ('model_C', 0.88)]
di = sorted(li, key=lambda x: x[1],reverse=True )
print(di)