package JavaTesting;
import java.util.Set;
import java.util.HashSet;
import java.util.Iterator;

public class javaTestingSite {

    public static void main(String[] args) {
        Set<String> hashSet = new HashSet<String>();

        hashSet.add("Thing one");
        hashSet.add("hi");
        hashSet.add("Thing two");
        hashSet.remove("hi");
        
        Iterator<String> hashItem = hashSet.iterator();

        while (hashItem.hasNext()) {
            System.out.println(hashItem.next() + " ");
        }
        
    }
}