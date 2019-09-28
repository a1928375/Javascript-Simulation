javascriptcode="""
function gcd(a,b) {
    
    if (a==b) {
        return a;
    } else if (a>b) {
        return gcd(a-b,b);
    } else {
        return gcd(a,b-a);
    }
}


write( gcd(24,8) == 8 ); 
write(" ");
write( gcd(1362, 1407) );
write( gcd(1875, 1907) );
write(" ");
write( gcd(45,116) ); 
"""
