package SortingAlgorithms;

//written by Elliott Wink
//https://en.wikipedia.org/wiki/Insertion_sort

public class InsertionSort{
 private int[] arr;
 private int checks, swaps;
 private final int INITIAL_SIZE = 50;

 public InsertionSort() {
     checks = 0;
     swaps = 0;
     arr = new int[INITIAL_SIZE];
     for(int i = 0; i < 50; ++i) {
         arr[i] = (int)(Math.random() * 100);
     }
     arr = sort();
 }

 public InsertionSort(int[] arr) {
     checks = 0;
     swaps = 0;
     this.arr = arr;
     this.arr = sort();
 }

 public int[] sort(){
     for(int i = 1; i < arr.length; ++i) {
         int toPlace = i, current = arr[i];
         for(int j = i - 1; j > 0 && arr[j] >= arr[i]; --j) {
             arr[toPlace] = arr[j];
             toPlace = j;
             ++checks;
         }
         arr[toPlace] = current;
         ++swaps;
     }
     return arr;
 }

 public int[] getSortedArray(){return arr;}

 public int getChecks(){return checks;}

 public int getSwaps(){return swaps;}

 public int bestCase(){return arr.length;}

 public int averageCase(){return (int)(Math.pow(arr.length, 2));}

 public int worstCase(){return (int)(Math.pow(arr.length, 2));}
}