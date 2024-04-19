package Picnic;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;


/**Класс считывает данные из файла и подготавливает их к обработке 
 * (убирает лишние пробелы, делает все слова с заглавных букв)
 * Возвращает массив строк, где строка это слово из файла
 */
public class Reader {
    String[] words;


    public Reader(){

    }

    /**Функция, проверяющая, чтобы слова начинались с заглавных букв
     * @param word Слово для проверки
     * @return Исправленное слово
     */
    public String firstUpperCase(String word){
        if(word == null || word.isEmpty()) return "";
        return word.substring(0, 1).toUpperCase() + word.substring(1);
    }

    /**Запускает чтение из файла
     * @param file Файл из которого читаем
     * @return Массив строк, парсится из файла через пробел
     */
    public String[] run(File file){
        try{
            FileReader fr = new FileReader(file);
            BufferedReader reader = new BufferedReader(fr);
            String line = reader.readLine();
            words = line.split("\\s+");
            for (int i = 0; i<words.length; i++){
                words[i] = firstUpperCase(words[i]);
            }
            reader.close();
        }
        catch (Exception e){
            System.out.println(e.getMessage());
        }
        return words;
    }
}
