import React from "react";
import { useState, useEffect } from "react";

async function getArticles(): Promise<any> {
    try {
        const response = await fetch('http://localhost:3000/articles');
        
        if (!response.ok) {
            throw new Error(`Error, status: ${response.status}`);
        }
        const articles = await response.json();

        console.log(articles);
    } catch (error: any) {
        console.error('Failed to fetch articles:', error.message);
    }
}

function Home() {

    const [articleData, setArticleData] = useState('')

    useEffect(() => {
        getArticles();
    }, [])

    return (
        <>
            <h1>Home</h1>
        </>
    )
}

export default Home;