package com.rjf

import java.sql.DriverManager
const val DERIVED_EMB_SIZE = 100 // Replace with actual size

fun main() {

    fun main() {
//        val url = "jdbc:postgresql://localhost:5432/postgres"
//        val user = "postgres"
//        val password = "postgres"
//
//
//        // Creation of Table
//        DriverManager.getConnection(url, user, password).use { conn ->
//            conn.createStatement().use { stmt ->
//                stmt.execute("CREATE TABLE items (id bigserial PRIMARY KEY, text TEXT, embedding vector($DERIVED_EMB_SIZE));")
//            }
//        }
//
//        // Insertion Of Records
//        val documents = listOf<String>() // Your list of sentences
//        val embeddings = listOf<List<Float>>() // Your list of embeddings
//        DriverManager.getConnection(url, user, password).use { conn ->
//            conn.prepareStatement("INSERT INTO items(id, text, embedding) VALUES (?, ?, ?)").use { stmt ->
//                for ((index, item) in documents.withIndex()) {
//                    stmt.setInt(1, index)
//                    stmt.setString(2, item)
//                    stmt.setArray(3, conn.createArrayOf("float", embeddings[index].toTypedArray()))
//                    stmt.executeUpdate()
//                }
//            }
//        }
//
//        // Retrieval
//        DriverManager.getConnection(user, user, password).use { conn ->
//            conn.prepareStatement("SELECT text, 1 - (embedding <=> ?) AS cosine_similarity FROM items ORDER BY 2 DESC").use { stmt ->
//                stmt.setString(1, userQueryEmbedding.toString())
//
//                val rs = stmt.executeQuery()
//                while (rs.next()) {
//                    val text = rs.getString("text")
//                    val cosineSimilarity = rs.getDouble("cosine_similarity")
//                    println("$text $cosineSimilarity")
//                }
//            }
//        }
    }

}