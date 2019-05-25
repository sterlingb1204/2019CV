import java.util.*;

public class Statistics
{
	public static void main(String[] args)
	{
		System.out.println("Welcome to Statistics!");   // welcome
		System.out.println("This program will calculate the average, median, ");
		System.out.println("mode, and most of any number of (double) values!");
		System.out.println();
		Scanner input = new Scanner(System.in);   // scanner implementation
		System.out.print("How many values will you be entering? ");
		int vals = input.nextInt();
		System.out.println();
		double[] values = new double[vals]; // declaration of array "values" and loop assigns each value number to the array 
		for(int i = 0; i < vals; i++)
		{
			System.out.print("Please enter value #" + (i + 1) + ": ");
			values[i] = input.nextDouble();
		}
		System.out.println();
		ArrayHelper.display(values); // displays the results of the input numbers
		System.out.println();
		System.out.println("Average: " + average(values));
		System.out.print("Median: ");
		System.out.println(median(values));
		System.out.print("Mode: ");
		ArrayHelper.display(mode(values));
		System.out.println();
		System.out.print("Most: ");
		ArrayHelper.display(most(values));
	}
	
	public static double average(double[] values)
	{
		double sum = 0; // calculates sum, then divides by length of array
		for(int i = 0; i < values.length; i++)
		{
			sum += values[i];
		}
		return (sum / values.length);
	}
	
	public static double median(double[] values)
	{
		values = sort(values);
		if(values.length % 2 == 1)
			return values[values.length / 2]; // finds the median if the user inputs an odd number of values
		else
			return (values[values.length / 2] + values[(values.length / 2) - 1]) / 2;	// finds the median if even number of values
	}
	
  	public static double[] mode(double[] values)
   {
      values = sort(values);
      int count = 1;
      for(int i = 1; i < values.length; i++) // figures out amount of different numbers 
      {
         if(values[i] != values[i-1])
            count++;
      }
      double[] key = new double[count]; // loop gives values to array "key", which lists the different numbers 
      key[0] = values[0];
      int x = 1;
      for(int i = 1; i < values.length; i++)
      {
         if(values[i] != values[i-1])
         {
            key[x] = values[i];
            x++;
         }
         if(x == key.length)
            break;
      }
      double[] keyFreq = new double[key.length]; // array "keyFreq" counts the amount of times each number in "key" appears in "values"
      
      for(int i = 0; i < key.length; i++)
      {
         keyFreq[i] = ArrayHelper.count(values, key[i]);
      }
      double[] mode = new double[values.length]; // array "mode" lists the number(s) that appear the most in "values"
      x = 0;
      for(int i = 0; i < keyFreq.length; i++)
      {
         if(keyFreq[i] == ArrayHelper.max(keyFreq))
         {
            mode[x] = key[i];
            x++;
         }
      }
      mode = ArrayHelper.subArray(mode, 0, x); // trims "mode" so it is only as long as the amount of modes in "values"
      return mode;
   }

	
	public static double[] most(double[] values)
	{
		double average = ArrayHelper.average(values); // figures out average of "values"
		int count = 0;
		for(int i = 0; i < values.length; i++) // counts number of values that are greater than the average
		{
			if(values[i] > average)
				count++;
		}
		double[] most = new double[count];
		int x = 0;
		for(int i = 0; i < values.length; i++) // puts each value that is greater than the average into the array "most"
		{
			if(values[i] > average)
			{
				most[x] = values[i];
				x++;
			}	  
		}
		return most;
	}
	
	// returns a sorted copy of values
	// does not modify vaules
	public static double[] sort(double[] values)
	{
		double[] temp = values.clone();
		Arrays.sort(temp);
		return temp;
	}
}