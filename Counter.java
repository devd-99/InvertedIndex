public class Counter
{
	public static void main(String args[])
	{
		Scanner sc = new Scnner(System.in);
		int n = sc.nextInt();
		System.out.println(constSearch(n));
		System.out.println(logSearch(n));
		System.out.println(linearSearch(n));
		System.out.println(nlogSearch(n));
		System.out.println(polySearch(n));
		System.out.println(expSoearch(n));

	}

	public int constSearch(int n)
	{	
		return 1;
	}

	public int logSearch(int n)
	{
		int counter=0;
		for(int i=0;i<Math.log10(n);i++)
		{
			counter++;
		}
		return counter;
	}

	public int linearSearch(int n)
	{
		return n;
	}

	public int nlogSearch
	{
		int counter=0;
		for(int i=0;i<n;i++)
		{
			for(int j=0;j<Math.log10(n);j++)
			{
				counter++;
			}
		}
		return counter;
	}

	public int polySearch(int n)
	{
		return 0;
	}

	public int expoSearch(int n)
	{
		int counter=0;
		for(int i=0;i<Math.pow(2,n);i++)
		{
			counter++;
		}
		return counter;
	}



}