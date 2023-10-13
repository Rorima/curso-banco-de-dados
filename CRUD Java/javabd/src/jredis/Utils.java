package jredis;

import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;
import java.util.Set;

import redis.clients.jedis.Jedis;
import redis.clients.jedis.exceptions.JedisConnectionException;

public class Utils {

    static Scanner teclado = new Scanner(System.in);

    public static String gera_id() {
        Jedis conn = conectar();
        String chave = conn.get("chave");
        System.out.println("Chave: " + chave);
        System.out.println();
        
        if (chave != null) {
            chave = "" + conn.incr("chave");
            desconectar(conn);
            return chave;
        } else {
            conn.set("chave", "1");
            desconectar(conn);
            return "1";
        }
    }

    public static Jedis conectar() {
        Jedis conn = new Jedis("redis://localhost:6379/");
        return conn;
    }

    public static void desconectar(Jedis conn) {
        conn.disconnect();
    }
    
    public static void listar() {
        Jedis conn = conectar();

        try {
            Set<String> res = conn.keys("produtos:*");

            if (res.size() > 0) {
                System.out.println("Listando produtos\n");
                for (String chave: res) {
                    Map<String, String> produto = conn.hgetAll(chave);
                    System.out.println("ID: " + chave);
                    System.out.println("Produto: " + produto.get("nome"));
                    System.out.println("Preço: " + produto.get("preco"));
                    System.out.println("Estoque: " + produto.get("estoque"));
                    System.out.println();
                }
            } else {
                System.out.println("Não existem produtos cadastrados.");
            }
        } catch (JedisConnectionException e) {
            System.out.println("Verifique se o servidor Redis está ativo.\n" + e);
        }

        desconectar(conn);
    }

    public static void inserir() {
        Jedis conn = conectar();

        System.out.println("Digite o nome do produto: ");
        String nome = teclado.nextLine();

        System.out.println("Digite o preço do produto: ");
        String preco = teclado.nextLine();

        System.out.println("Digite a quantidade em estoque: ");
        String estoque = teclado.nextLine();

        Map<String, String> produto = new HashMap<String, String>();

        produto.put("nome", nome);
        produto.put("preco", preco);
        produto.put("estoque", estoque);

        String chave = "produtos:" + Utils.gera_id();

        try {
            String res = conn.hmset(chave, produto);

            if (res != null) {
                System.out.println("O produto '" + nome + "' foi inserido com sucesso!");
            } else {
                System.out.println("Não foi possível inserir o produto.");
            }
        } catch (JedisConnectionException e) {
            System.out.println("Verifique se o Redis está ativo.\n" + e);
        }
        desconectar(conn);
    }

    public static void atualizar() {
        Jedis conn = conectar();

        System.out.println("Digite a chave do produto: ");
        String chave = teclado.nextLine();

        System.out.println("Digite o nome do produto: ");
        String nome = teclado.nextLine();

        System.out.println("Digite o preço do produto: ");
        String preco = teclado.nextLine();

        System.out.println("Digite a quantidade em estoque: ");
        String estoque = teclado.nextLine();

        Map<String, String> produto = new HashMap<String, String>();

        produto.put("nome", nome);
        produto.put("preco", preco);
        produto.put("estoque", estoque);

        try {
            String res = conn.hmset(chave, produto);

            if (res != null) {
                System.out.println("O produto '" + nome + "' foi atualizado com sucesso!");
            } else {
                System.out.println("Não foi possível atualizar o produto.");
            }
        } catch (JedisConnectionException e) {
            System.out.println("Verifique se o Redis está ativo.\n" + e);
        }
        desconectar(conn);
    }

    public static void deletar() {
        Jedis conn = conectar();

        System.out.println("Digite a chave do produto: ");
        String chave = teclado.nextLine();

        try {
            Long red = conn.del(chave);

            if (red > 0) {
                System.out.println("O produto foi deletado com sucesso!");
            } else {
                System.out.println("O produto com a chave informada não existe.");
            }
        } catch (JedisConnectionException e) {
            System.out.println("Verifique se o Redis está ativo.\n" + e);
        }

        desconectar(conn);
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