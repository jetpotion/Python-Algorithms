function C = strassenMulti(MatrixA, MatrixB, minimum)
%We need the column length
n = length(MatrixA);

%If the columns are less than equal to 8 we cannot break into 4 parts
%equally. Assuming the N  X  N matrix we cannot break into 4 parts
if n <= minimum
   C = MatrixA*MatrixB;
else
    %M is  variable which divides the matrix posistion by in half
    %H is a variable to to traverse rows 
    %J is a variable to get the next ement in the row 
   m = n/2; h= 1:m; j = m+1:n;
   %Compute individual parts according the strassen diagram 
   P1 = strassenMulti( MatrixA(h,h)+MatrixA(j,j), MatrixB(h,h)+MatrixB(j,j), minimum);
   P2 = strassenMulti( MatrixA(j,h)+MatrixA(j,j), MatrixB(h,h), minimum);
   P3 = strassenMulti( MatrixA(h,h), MatrixB(h,j)-MatrixB(j,j), minimum);
   P4 = strassenMulti( MatrixA(j,j), MatrixB(j,h)-MatrixB(h,h), minimum);
   P5 = strassenMulti( MatrixA(h,h)+MatrixA(h,j), MatrixB(j,j), minimum);
   P6 = strassenMulti( MatrixA(j,h)-MatrixA(h,h), MatrixB(h,h)+MatrixB(h,j), minimum);
   P7 = strassenMulti( MatrixA(h,j)-MatrixA(j,j), MatrixB(j,h)+MatrixB(j,j), minimum);
   
   
   %In matlab you are able to divide the matrix into 4 parts 
   %Remember the diagram. The upper left is P1+P4 + P5 + P7 
   %The upper right and bottom left is is P3 +P5, P2+P4 respectively
   %The bottom right is( P1 + P3 ) - (P2 + P6)
   C = [ P1+P4-P5+P7  P3+P5;  P2+P4  P1+P3-P2+P6 ];
end
