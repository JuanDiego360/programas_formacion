using Tensorial
I=Mat{2,2}([1 0;0 1])
sx=Mat{2,2}([0 1; 1 0])
pro=(I ⊗ sx)⊗sx
pro