/*
 * Elliott Wink
 * https://en.wikipedia.org/wiki/Quicksort
 */

package SortingAlgorithms;

public class QuickSort {
    private int[] arr;
    private int checks, swaps;
    private final int INITIAL_SIZE = 50;
    
    public QuickSort() {
        checks = 0;
        swaps = 0;
        arr = new int[INITIAL_SIZE];
        for(int i = 0; i < INITIAL_SIZE; ++i) {
            arr[i] = (int)(Math.random() * 100);
        }
        arr = sort(arr, 0, arr.length - 1);
    }
    
    public QuickSort(int[] array) {
    	checks = 0;
        swaps = 0;
        arr = new int[INITIAL_SIZE];
        arr = array;
        arr = sort(arr, 0, array.length - 1);
    }
    
    private int[] sort(int[] array, int lo, int hi) {
    	if(lo < hi) {
    		int p = partition(array, lo, hi);
    		sort(array, lo, p - 1);
    		sort(array, p + 1, hi);
    	}
    	return array;
    }
    
    private int partition(int[] array, int lo, int hi) {
    	int pivot = array[hi];
    	int i = lo;
    	for(int j = i; j < hi; ++j) {
    		++checks;
    		if(array[j] < pivot) {
    			int copy = array[j];
    			array[j] = array[i];
    			array[i] = copy;
    			++i;
    			++swaps;
    		}
    	}
    	int copy = array[i];
    	array[i] = array[hi];
    	array[hi] = copy;
    	++swaps;
    	return i;
    }
    
    public int[] getArray(){return arr;}

    public int getChecks(){return checks;}

    public int getSwaps(){return swaps;}

    public int bestCase(){return arr.length * (int)(Math.log(arr.length));}

    public int averageCase(){return arr.length * (int)(Math.log(arr.length));}

    public int worstCase(){return (int)(Math.pow(arr.length, 2));}
}
