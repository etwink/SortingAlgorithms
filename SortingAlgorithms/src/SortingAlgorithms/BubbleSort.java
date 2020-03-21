package SortingAlgorithms;
// written by Elliott Wink
// https://en.wikipedia.org/wiki/Bubble_sort


public class BubbleSort {
    private int[] arr;
    private int checks, swaps;
    private final int INITIAL_SIZE = 50;

    public BubbleSort() {
        checks = 0;
        swaps = 0;
        arr = new int[INITIAL_SIZE];
        for(int i = 0; i < 50; ++i) {
            arr[i] = (int)(Math.random() * 100);
        }
        arr = sort();
    }

    public BubbleSort(int[] arr) {
        checks = 0;
        swaps = 0;
        this.arr = arr;
        this.arr = sort();
    }

    private int[] sort() {
        int tmp;
        checks = 0;
        for(int i = 0; i < arr.length; ++i) {
            for(int j = 0; j < arr.length - i - 1; j++) {
                if(arr[j] > arr[j+1]) {
                    tmp = arr[j + 1];
                    arr[j + 1] = arr[j];
                    arr[j] = tmp;
                    ++swaps;
                }
                ++checks;
            }
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