package jmysql;

import java.sql.Connection;
import java.sql.DriverManager;
import java.util.Scanner;

public class Utils {

    static Scanner teclado = new Scanner(System.in);

    public static Connection conectar() {
        String CLASSE_DRIVER = "com.mysql.jdbc.Driver";
        String USUARIO = "roni";
        String SENHA = "roni";
        String URL_SERVIDOR = "jdbc:mysql://localhost:3306/jmysql?useSSL=false";

        try {
            Class.forName(CLASSE_DRIVER);
            return DriverManager.getConnection(URL_SERVIDOR, USUARIO, SENHA);
        } catch(Exception e) {
            if (e instanceof ClassNotFoundException) {
                System.out.println("Verifique o driver de conexão.");
            } else {
                System.out.println("Verifique se o servidor está ativo.");
            }

            System.exit(-42);
            return null;
        }
    }

    public static void desconectar() {
        System.out.println("Desconectando...");
    }
    
    public static void listar() {
        System.out.println("Listando produtos...");
    }

    public static void inserir() {
        System.out.println("Inserindo produtos...");
    }

    public static void atualizar() {
        System.out.println("Atualizando produtos...");
    }

    public static void deletar() {
        System.out.println("Deletando produtos...");
    }

    public static void menu() {
        System.out.println("======== Gerenciamento de Produtos ========");
        System.out.println("Selecione uma opção: ");
        System.out.println("1 - Listar produtos;");
        System.out.println("2 - Inserir produtos;");
        System.out.println("3 - Atualizar produtos;");
        System.out.println("4 - Deletar produtos.");

        int opcao = Integer.parseInt(teclado.nextLine());
        if(opcao == 1) {
            listar();
        } else if (opcao == 2) {
            inserir();
        } else if (opcao == 3) {
            atualizar();
        } else if (opcao == 4) {
            deletar();
        } else {
            System.out.println("Opção inválida!");
        }
    }
}