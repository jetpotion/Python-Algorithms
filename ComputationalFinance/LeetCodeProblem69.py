#Using the classic newtons method, 
class Solution {
    public int mySqrt(int x) {
        if (x == 0) {
            return 0;
        }
        long r = x; // use `long` so r*r is calculated as a long
        
        while (r*r > x) {
            r = (r + x/r) / 2;
        }    	
        return (int) r;
    }
}
