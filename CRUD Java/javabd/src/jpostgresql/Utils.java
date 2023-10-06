package jpostgresql;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.Properties;
import java.util.Scanner;


public class Utils {

    static Scanner teclado = new Scanner(System.in);

    public static Connection conectar() {
        Properties props = new Properties();
        props.setProperty("user", "roni");
        props.setProperty("password", "roni");
        props.setProperty("ssl", "false");
        String URL_SERVIDOR = "jdbc:postgresql://localhost:5432/jpostgresql";

        try {
            return DriverManager.getConnection(URL_SERVIDOR, props);
        } catch (Exception e) {
            e.printStackTrace();

            if (e instanceof ClassNotFoundException) {
                System.err.println("Verifique o driver de conexão.");
            } else {
                System.err.println("Verifique se o servidor está ativo.");
            }

            System.exit(-42);
            return null;
        }
    }

    public static void desconectar(Connection conn) {
        if (conn != null) {
            try {
                conn.close();
            } catch (SQLException e) {
                e.printStackTrace();
            }
        }
    }
    
    public static void listar() {
        String BUSCAR_TODOS = "SELECT * FROM produtos";

        try {
            Connection conn = conectar();
            PreparedStatement produtos = conn.prepareStatement(
                BUSCAR_TODOS, ResultSet.TYPE_SCROLL_INSENSITIVE, 
                ResultSet.CONCUR_READ_ONLY
            );
            
            ResultSet res = produtos.executeQuery();
            res.last();
            int qtd = res.getRow();
            res. beforeFirst();

            if (qtd > 0) {
                System.out.println("Listando produtos:\n");
                System.out.println("ID: " + res.getInt(1));
                System.out.println("Produto: " + res.getString(2));
                System.out.println("Preço: " + res.getFloat(3));
                System.out.println("Estoque: " + res.getInt(4));
                System.out.println("");
            } else {
                System.out.println("Não existem produtos cadastrados.");
            }

        } catch (Exception e) {
            e.printStackTrace();
            System.err.println("Erro buscando todos os produtos.");
            System.exit(-42);
        }
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