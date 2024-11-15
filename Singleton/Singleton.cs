using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace Singleton
{

    class Program
{
    static void Main(string[] args)
    {
        Singleton s1 = Singleton.GetInstance();
        Singleton s2 = Singleton.GetInstance();

        Console.WriteLine(s1 == s2); // Deve exibir "True"
    }
}
    public class Singleton
{
    // A única instância da classe, privada e estática
    private static Singleton _instance;

    // Construtor privado para evitar criação externa de instâncias
    private Singleton()
    {
        Console.WriteLine("Instância criada");
    }

    // Método para obter a instância única, com verificação de instância
    public static Singleton GetInstance()
    {
        if (_instance == null)
        {
            _instance = new Singleton();
        }
        return _instance;
    }
}

}