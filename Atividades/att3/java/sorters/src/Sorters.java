/*
Apesar de poder separar em vários arquívos quero algo mais proximo do paradigma imperativo...
Desculpa pessoas...

Três quatro aqui: 
bubble_sort
merge_sort
merge
readFile

*/

package sorters;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.Arrays;
import java.util.Scanner;

public class Sorters {

    public static void main(String[] args) {
        int[] lista_a_ser_ordenada = readFile("../../../arq.txt");
        
        int[] BB = bubble_Sort(lista_a_ser_ordenada);
        int[] MS = merge_sort(lista_a_ser_ordenada);
        
        System.out.println(Arrays.toString(BB));
        System.out.println(Arrays.toString(MS));
    }

    public static int[] bubble_Sort(int[] lista)
    {
        int[] arr = lista;
        
        int n = arr.length;
        boolean swapped;
        
        for (int i = 0; i < n - 1; i++) {
            swapped = false;
            
            for (int j = 0; j < n - i - 1; j++) {
                if (arr[j] > arr[j + 1]) {
                    int temp = arr[j];
                    arr[j] = arr[j + 1];
                    arr[j + 1] = temp;
                    swapped = true;
                }
            }
            
            if (!swapped) {
                break;
            }
        }
        return arr;
    }

    public static int[] merge_sort(int[] lista)
    {   
        int len = lista.length;
        int med = (int) len / 2;
        int comp = len - med;
        int[] arr1 = new int[med];
        int[] arr2 = new int[comp];
        
        int[] oarr1 = new int[med];
        int[] oarr2 = new int[comp];
        if (len <= 1)
            return lista;
        
        // vou escolher nn usar o arraycopy :)
        for (int i = 0; i < med; i++){
            arr1[i] = lista[i];
        }
        for (int j = med; j < len; j++){
            arr2[j - med] = lista[j];
        }

        oarr1 = merge_sort(arr1);
        oarr2 = merge_sort(arr2);
        return merge(oarr1, oarr2);
        
    }

    private static int[] merge(int[] arr1, int[] arr2) {
        int n1 = arr1.length;
        int n2 = arr2.length;

        int[] orded = new int[n1 + n2]; 


        int i = 0; 
        int j = 0; 
        int k = 0;

        while (i < n1 && j < n2) {
            if (arr1[i] <= arr2[j]) {
                orded[k] = arr1[i];
                i++;
            } else {
                orded[k] = arr2[j];
                j++;
            }
            k++;
        }

        while (i < n1) {
            orded[k] = arr1[i];
            i++;
            k++;
        }

        while (j < n2) {
            orded[k] = arr2[j];
            j++;
            k++;
        }
        return orded;
    }
    public static int[] readFile(String path) {
        File arq = new File(path);
        int[] lista = new int[1024*1024];
        int len = 0; 
        try (Scanner Dados = new Scanner(arq)){
            while (Dados.hasNext()){
                lista[len] = Dados.nextInt();
                len++;
            }
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }
        return lista;
        }
}