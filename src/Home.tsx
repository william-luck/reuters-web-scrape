import React from "react";
import { useState, useEffect } from "react";


function Home() {

    const [articleData, setArticleData] = useState<any[]>([])

    useEffect(() => {
        getArticles();
    }, [])

    async function getArticles(): Promise<any> {
        try {
            const response = await fetch('http://localhost:3000/articles');
            
            if (!response.ok) {
                throw new Error(`Error, status: ${response.status}`);
            }
            const articles = await response.json();
            setArticleData(articles)
        } catch (error: any) {
            console.error('Failed to fetch articles:', error.message);
        }
    }

    function articleContent(data: any) {
        return (
            <>
                <h3>{data.title}</h3>
                <p>{data.content}</p>
                <br></br>
            </>
        )
    }

    return (
        <>
            <h1>Home</h1>

            <div>
                <div>
                    {articleData.length > 0 ? 
                        articleData.map(article => articleContent(article))
                        : null}
                </div>
            </div>
        </>
    )
}

export default Home;