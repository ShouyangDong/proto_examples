# proto_examples

# install procedure
  pip install protobuf
  
  
  Conv    - >        pool        -> dense
  
  
  Graph = [conv, pool, dense]
  Graph.outputs = dense
  dense.attribute[n, h, W, datatype]
  
  dense.op.inputs = [pool]
  
  pool.op.inputs = [Conv]


protobuf graph

graph[0] conv
graph[1] pool

1. runtime compile
2. 3layer   for i in 【buffer】:
              for j in configuration:
3. uni dis
   normal dis  U, sig: 
4. configuration
5. graph optimization  Nms  sigmoid  NMS   100  < 0.5   X
