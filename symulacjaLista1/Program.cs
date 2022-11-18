using System;
using System.Linq;
using Accord.Statistics.Visualizations;
using Accord.Controls;
using System.Windows;
using System.Collections.Generic;
using Newtonsoft.Json;
using System.IO;
using System.Threading;
namespace symulacjaLista1
{
    class Program
    {
        class Histogram
        {
            IEnumerable<KeyValuePair<string, int>> list;
            public System.Diagnostics.Process proc;
            public Histogram(string[] keys, int[] values)
            {
                
                if (keys.Length == values.Length)
                {
                    list = new List<KeyValuePair<string, int>>();
                    for (int i = 0; i <keys.Length; i++)
                    {
                        list = list.Append(new KeyValuePair<string, int>(keys[i], values[i]));
                    }
                }
                else { throw new Exception("różna ilość wartości i etykiet"); }
            }
            public void Show() {
                string jsonstring = JsonConvert.SerializeObject(list);
                
                string path = Path.GetTempFileName();
                File.WriteAllText(path, jsonstring);
                proc = System.Diagnostics.Process.Start("C:\\Users\\Przemek\\source\\repos\\symulacjaLista1\\histogram\\run.bat", "C:\\Users\\Przemek\\source\\repos\\symulacjaLista1\\histogram\\histogram.py " + path);
            }
            public void Close() {
                proc.Close();
            }
        }
        enum KamienPapierNozyce
        {
            kamien = 0,
            papier = 1,
            nozyce = 2
        }
        enum Wygrana
        {
            W = 0,
            L = 1,
            remis = 2
        }

     

        static void Main(string[] args)
        {
            Zad2();
        }
        static void Zad2()
        {

            ulong m = (ulong)Math.Pow(2, 16) + 1;
            RandomNum generator = new RandomNum(75, 74, m, 2);
            KPN gra = new KPN();
            Wygrana[] wyniki = new Wygrana[100];
            for (int n = 0; n < 100; n += 1)
            {
                wyniki[n] = gra.Graj((KamienPapierNozyce)generator.GenNext(0, 2), (KamienPapierNozyce)generator.GenNext(0, 2));
            }

            var wygrane = from wynik in wyniki where wynik == Wygrana.W select wynik;
            var przegrane = from wynik in wyniki where wynik == Wygrana.L select wynik;
            var remisy = from wynik in wyniki where wynik == Wygrana.remis select wynik;
            Console.WriteLine("W:" + wygrane.Count().ToString() + " L:" + przegrane.Count().ToString() + " R:" + remisy.Count().ToString());

            Histogram hist = new Histogram(new string[] { "W:", "L:", "R:" },
                new int[] { wygrane.Count(), przegrane.Count(), remisy.Count() });
            hist.Show();
            hist.proc.Exited += Zad3;
            while (!hist.proc.HasExited)
            {
                Thread.SpinWait(1000);
            }

            Console.WriteLine(Environment.NewLine + Environment.NewLine + "######################");
        }

        private static void Zad3(object sender, EventArgs e)
        {
            Console.WriteLine("dudek");
        }

        class KPN
        {
            public KPN()
            {

            }
            public Wygrana Graj(KamienPapierNozyce gracz1, KamienPapierNozyce gracz2)
            {
                if (gracz1 == gracz2)
                {
                    return Wygrana.remis;
                }
                if ((gracz1 == KamienPapierNozyce.kamien && gracz2 == KamienPapierNozyce.nozyce) ||(gracz1 == KamienPapierNozyce.nozyce && gracz2 == KamienPapierNozyce.papier) ||(gracz1 == KamienPapierNozyce.papier && gracz2 == KamienPapierNozyce.kamien))
                {
                    return Wygrana.W;
                }
                return Wygrana.L;
            }
        }
        class RandomNum
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
                x = (seed*a+c)%m;
            }
            public ulong GenNext()
            {
                x = (x * a + c) % m;
                return x;
            }
            public ulong GenNext(ulong min, ulong max)
            {
                x = (x * a + c) % m;
                return (ulong)min + (ulong)Math.Floor((double)x/(double)m*(max-min+1));
            }
        }

        class GraKosci
        {
            int wygrane;
            int przegrane;
        }
    }
}
