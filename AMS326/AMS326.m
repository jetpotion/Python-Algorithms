
%MatrixA
matrixa  = -2 + (2+2)*rand(1024);
%MatrixB
matrixb  = -2 +(2+2) * rand(1024);

%The matrix we want to input to
matrixc = zeros(1024,1024);

%Perform the brute multuplication between two matrices 
N = 1024
for i = 1:N
    for j = 1:N
        for k = 1:N
            matrixc(i,j)  = matrixc(i,j) + matrixa(i,k) * matrixb(k,j);
        end
    end
end
%This variable confirms that the brute force matrix multiplication works
testmatrix = matrixa * matrixb;

%This time employ strassen method 
strassenmatrix =  strassenMulti(matrixa,matrixb,8);



