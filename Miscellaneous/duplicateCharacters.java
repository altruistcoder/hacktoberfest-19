public class duplicateCharacters {


    public static void main(String arg[]) {

        final String s = "hacktoberfest";
        return findDuplicate(s);

    }

    public String findDuplicate(final String s) {
        char[] charArr = s.toCharArray();
        for(int i = 0; i < s.length(); i++) {
            for(int j = i + 1; j < s.length(); j++) {
                if (charArr[i] == charArr[j]) {
                    System.out.println(charArr[j]);
                }
            }
        }

    }


}