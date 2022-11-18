using System;

namespace lista2
{
    class Program
    {
        static Random rnd = new Random();
        static uint SimulateWall(ushort hole_nr)
        {
            uint[] values = new uint[] { 1000, 10, 2000, 1, 5000, 1, 2000, 10, 1000 };
            uint[] distribution = new uint[] { 1, 5, 11, 15, 16 };
            int random = rnd.Next(1, 5);
            int i = 0;
            while (true)
            {
                if (distribution[i] >= random) { return values[i + hole_nr - 1]; };
                i += 1;
            }

        }
        static double CalculateExpectedValue(ushort hole_nr, bool swap_5000_to_500 = false)
        {
            uint[] values = new uint[] { 1000, 10, 2000, 1, 5000, 1, 2000, 10, 1000 };
            if (swap_5000_to_500) { values[4] = 500; }
            uint[] distribution = new uint[] { 1, 4, 6, 4, 1 };
            int sum = 0;
            for (int i = 0; i < 5; i++)
            {
                sum += (int)(values[i + hole_nr - 1] * distribution[i]);
            }
            return (double)sum / 16;
        }
        static void Zad3i4(bool zad4)
        {
            double[] best = { 0, 0 };
            for (ushort i = 1; i <= 5; i++)
            {
                if (best[0] == CalculateExpectedValue(i, zad4))
                {
                    Console.WriteLine("Multiple holes that lead to same expected value: " + best[1].ToString() +" and "+ i.ToString());
                }
                if (best[0] < CalculateExpectedValue(i,zad4))
                {
                    best[0] = CalculateExpectedValue(i,zad4);
                    best[1] = i;
                }
                
            }
            Console.WriteLine(best[0].ToString() + " " + best[1].ToString());
        }

        static void Main(string[] args)
        {
            Console.WriteLine(SimulateWall(1)); //Zad1
            Console.WriteLine(CalculateExpectedValue(3));//Zad2
            Zad3i4(false);//Zad3
            Zad3i4(true);//Zad4
        }
    }
}
