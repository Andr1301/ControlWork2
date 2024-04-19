package Picnic;

import java.io.File;

public class Picnic {

    public static void main(String[] args) {
        File file = new File("Picnic\\Input.txt");
        Reader reader = new Reader();
        String[] words = reader.run(file);
        Analyzer analyzer = new Analyzer();
        analyzer.run(words);
    }
}