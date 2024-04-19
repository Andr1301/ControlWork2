package Picnic;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Set;

/**Анализирует данные из файла
 * 
 */
public class Analyzer {

    String longestWord;
    
    public Analyzer() {
        
    }
    
    public void run(String[] products){
        
        HashMap<String, Integer> picnic = new HashMap<>();
        
        for (String word : products){  //Заполняем HashMap значениями
            if(picnic.containsKey(word)){
                int value = picnic.get(word)+1;
                picnic.put(word, value);
            }
            else{
                picnic.put(word, 1);
            }
        }
        System.out.println("Что мы принесли с собой на пикник:");
        for(HashMap.Entry<String, Integer> entry : picnic.entrySet()){
            System.out.println(entry);
        }
        
        Set<String> keys = picnic.keySet();  //Вычисляем самое длинное слово (или несколько)
        List<String> list = new ArrayList<>(keys); 
        
        longestWord = list.get(0);
        int l = longestWord.length();
        for (String word : list){
            if (word.length() > l){
                l = word.length();
            }
        }

        String[] longest = new String[picnic.size()]; //Используем массив на случай, если будет несколько длинных слов
        int i = 0;
        for (String word : list){
            if (word.length() == l){
                longest[i] = word;
                i++;
            }
        }
        System.out.println("Разных продуктов на пикнике: " + picnic.size());
        System.out.println("Всего продуктов на пикнике: " + products.length);
        System.out.println("Самые длинные слова (длина = " + l + "): ");
        for (String word : longest){
            if (word != null){
                System.out.println(word);
            }
        }
    }
}
