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
