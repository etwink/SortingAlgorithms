package SortingAlgorithms;

//written by Elliott Wink
//https://en.wikipedia.org/wiki/Merge_sort

public class MergeSort {
 private int[] arr;
 private int checks, swaps, splits;
 private final int INITIAL_SIZE = 50;

 public MergeSort() {
     checks = 0;
     swaps = 0;
     arr = new int[INITIAL_SIZE];
     for(int i = 0; i < 50; ++i) {
         arr[i] = (int)(Math.random() * 100);
     }
     arr = sort(arr);
 }

 public MergeSort(int[] arr) {
     checks = 0;
     swaps = 0;
     this.arr = arr;
     this.arr = sort(this.arr);
 }

 private int[] sort(int[] arr) {
     int[] first = new int[arr.length/2], second = new int[arr.length/2 + arr.length%2];
     if(arr.length > 1){
         for(int i = 0; i < first.length; ++i) {
             first[i] = arr[i];
             second[i] = arr[i + arr.length/2];
         }
         if(arr.length%2 != 0) {second[arr.length/2] = arr[arr.length - 1];}
         if(first.length > 1) {
             ++splits;
             sort(first);
         }
         if(second.length > 1) {
             ++splits;
             sort(second);
         } 
     }
     else return arr;
     int firstCount = 0, secondCount = 0, sortedCount = 0;
     while(firstCount != first.length && secondCount != second.length) {
         if((firstCount < first.length && secondCount < second.length && first[firstCount] > second[secondCount]) || (secondCount >= second.length)) {
             arr[sortedCount] = first[firstCount];
             ++firstCount;
             ++sortedCount;
             ++swaps;
             ++checks;
         }
         else if((firstCount < first.length && secondCount < second.length && first[firstCount] <= second[secondCount]) || (firstCount >= first.length)) {
             arr[sortedCount] = second[secondCount];
             ++secondCount;
             ++sortedCount;
             ++swaps;
             ++checks;
         }
     }
     return arr;
 }

 public int[] getarray(){return arr;}

 public int getChecks(){return checks;}

 public int getSwaps(){return swaps;}

 public int getSplits(){return splits;}

 public int bestCase(){return arr.length * (int)(Math.log(arr.length));}

 public int averageCase(){return arr.length * (int)(Math.log(arr.length));}

 public int worstCase(){return arr.length * (int)(Math.log(arr.length));}
}