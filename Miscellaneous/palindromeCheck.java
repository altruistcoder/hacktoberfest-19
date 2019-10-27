public class palindromeCheck {

    public static void main(String args[]) {
        final String isPalindrome = "anna";
        final String isNotPalindrome = "Fire Emblem Three Houses";
        System.out.println(isAPalindrome(isPalindrome));
        System.out.println(isAPalindrome(isNotPalindrome));
    }


    public boolean isAPalindrome(final String s) {
        StringBuffer buffer = new StringBuffer(s);
        buffer.reverse();
        if(buffer.equal(s)) {
            return true;
        } else {
            return false;
        }

    }



}