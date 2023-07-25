package com.ccc.book.service;

import com.ccc.book.model.Book;

import java.util.List;

public interface BookService {
    List<Book> getAllBooks();
    Book getBookById(Long id);
    Book saveBook(Book book);
    Book updateBook(Long id, Book updatedBook);
    void deleteBook(Long id);
}
