using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Lista3
{
    class Program
    {
        public class RandomNum
        {
            private uint a;
            private uint c;
            private ulong m;
            private ulong x;

            public RandomNum(uint a, uint c, ulong m, ulong seed)
            {
                this.a = a;
                this.c = c;
                this.m = m;
                x = (seed * a + c) % m;
            }
            public ulong GenNext()
            {
                
                x = (x * a + c) % m;
                return x;
            }
            public ulong GenNext(ulong min, ulong max)
            {
                x = (x * a + c) % m;
                return (ulong)min + (ulong)Math.Floor((double)x / (double)m * (max - min + 1));
            }
            public int GenPoisson(double lbd)
            {
                double L, p, u;
                int k;

                L = Math.Exp(-lbd);
                k = 0;
                p = 1;
                do
                {
                    k = k + 1;
                    u = (double)GenNext()/this.m;
                    p = p * u;
                } while (p > L);

                return (k - 1);
            }
        }
        public class Carbon14
        {
            public double halfLife { get; }
            public ushort accuracyOfSimulation { get; set; }
            public double oneStepTime { get; }
            public double currentTimeInSimulation { get; set; }

            public Carbon14(ushort accuracy)
            {
                currentTimeInSimulation = 0;
                halfLife = 5730;
                oneStepTime = halfLife;
                accuracyOfSimulation = accuracy;
                for (; accuracy > 0; accuracy--){
                    oneStepTime /= 2;
                }
            }
        }

        public class Cats
        {
            public RandomNum generator { get; set; }
            public List<double> livingTime { get; }
            public uint count { get; }
            public uint countLiving { get; set; }
            
            public Cats(uint count)
            {
                livingTime = new List<double>();
                countLiving = count;
                
                
            }
            public void DoOneStep(ref Carbon14 węgiel)
            {
                
                for (int i =(int) countLiving; i >= 0; i--)
                {
                    ulong stała = (ulong)Math.Pow(2, 16 - węgiel.accuracyOfSimulation);
                    ulong dupa = generator.GenNext();
                    if (dupa < stała){
                        countLiving--;
                        Console.WriteLine("cat died, current time: " + węgiel.currentTimeInSimulation.ToString() + "  cats left: " + countLiving.ToString());
                        livingTime.Add(węgiel.currentTimeInSimulation);
                    }
                }
                //Console.WriteLine(węgiel.currentTimeInSimulation.ToString());
                węgiel.currentTimeInSimulation += węgiel.oneStepTime;
            }
        }

        static void Zad1()
        {
            Carbon14 węgiel = new Carbon14(16);
            uint catNumber = 10000;
            ushort pValue = 65;
            Cats symulacja = new Cats(catNumber);
            ulong m = (ulong)Math.Pow(2, 16) + 1;
            symulacja.generator = new RandomNum(75, 74, m, 62);
            while (symulacja.countLiving > catNumber / 100 * 65)
            {
                symulacja.DoOneStep(ref węgiel);
            }
        }
        static void Zad2()
        {
            ulong m = (ulong)Math.Pow(2, 16) + 1;
            RandomNum generator = new RandomNum(75, 74, m, 62);
            List<int> people = new List<int>();
            for (int i = 0; i < 2000; i++)
            {
                string chart = "";
                for (int j = people.Count; j > 0; j--) { chart += '_'; }
                Console.WriteLine(chart);
                if (1==generator.GenPoisson(0.1))
                {
                    people.Add(generator.GenPoisson(8));
                }
                if (people.Count() == 0) { continue; }
                if (people[0] == 1) { people.Remove(1);continue; }
                people[0] -= 1;
            }
        }
        static void Main(string[] args)
        {
            //Zad1();
            Zad2();
            Console.ReadLine();
        }
    }
}
