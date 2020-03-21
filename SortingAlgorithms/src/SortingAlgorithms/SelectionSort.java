package SortingAlgorithms;

//written by Elliott Wink
//https://en.wikipedia.org/wiki/Selection_sort

public class SelectionSort{
 private int[] arr;
 private int checks, swaps;
 private final int INITIAL_SIZE = 50;

 public SelectionSort() {
     checks = 0;
     swaps = 0;
     arr = new int[INITIAL_SIZE];
     for(int i = 0; i < 50; ++i) {
         arr[i] = (int)(Math.random() * 100);
     }
     arr = sort();
 }

 public SelectionSort(int[] arr) {
     checks = 0;
     swaps = 0;
     this.arr = arr;
     this.arr = sort();
 }

 private int[] sort(){
     for(int i = 0; i < arr.length; ++i) {
         int min = arr[i], minLoc = i;
         for(int j = i; i < arr.length; ++j) {
             if(arr[j] < arr[i]) {
                 min = arr[j];
                 minLoc = j;
                 ++checks;
             }
         }
         if(min != arr[i] && minLoc != i) {
             arr[minLoc] = arr[i];
             arr[i] = min;
             ++swaps;
         }
     }
     return arr;
 }

 public int[] getSortedArray(){return arr;}

 public int getChecks(){return checks;}

 public int getSwaps(){return swaps;}

 public int bestCase(){return (int)(Math.pow(arr.length, 2));}

 public int averageCase(){return (int)(Math.pow(arr.length, 2));}

 public int worstCase(){return (int)(Math.pow(arr.length, 2));}
}