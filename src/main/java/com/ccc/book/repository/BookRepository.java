package com.ccc.book.repository;

import com.ccc.book.model.Book;
import org.springframework.data.jpa.repository.JpaRepository;

public interface BookRepository extends JpaRepository<Book, Long> {
    // Additional custom queries can be defined here if needed
}
