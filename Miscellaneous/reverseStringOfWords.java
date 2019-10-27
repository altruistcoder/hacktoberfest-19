public class reverseStringOfWords {

    public static void main(String[] args) {
        final String s = "Hacktoberfest 2019 Reverse String";
        return reverseString(s);
    }

    public String reverseString(final String s) {
        final String strArr [] = s.split(" ");
        final String result="";

        for (int i=strArr.length-1;i>=0;i--) {
            if(!strArr[i].trim().equals("")) {
                result += strArr[i]+" ";
            }
        }
        return result;
    }
}