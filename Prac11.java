import java.util.*;

public class Prac11 {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter the input set:");
        String input = scanner.nextLine();

        // Split the input into words
        String[] words = input.split("\\s+");

        // Create a map to store word frequencies
        Map<String, Integer> wordFrequencyMap = new HashMap<>();

        // Count the occurrences of each word
        for (String word : words) {
            word = word.replaceAll("[^a-zA-Z]", "").toLowerCase();
            // Update the frequency in the map
            wordFrequencyMap.put(word, wordFrequencyMap.getOrDefault(word, 0) + 1);
        }

        // Print the word frequencies
        System.out.println("Word Frequencies:");
        for (String word : wordFrequencyMap.keySet()) {
            System.out.println(word + ": " + wordFrequencyMap.get(word));
        }
    }
}
