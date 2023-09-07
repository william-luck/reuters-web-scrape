import React from "react";
import { useState, useEffect } from "react";


function Home() {

    const [articleData, setArticleData] = useState<any[]>([])

    useEffect(() => {
        getArticles();
    }, [])

    async function getArticles(): Promise<any> {
        try {
            const response = await fetch('http://localhost:3000/analysis');
            
            if (!response.ok) {
                throw new Error(`Error, status: ${response.status}`);
            }
            const articles = await response.json();
            setArticleData(articles[0].choices[0].message.content.split('\n'))
        } catch (error: any) {
            console.error('Failed to fetch articles:', error.message);
        }
    }

    return (
        <>
            <h1>Home</h1>

            <div>
                <div>
                    {articleData.length > 0 ? 
                        articleData.map(newLine => <p>{newLine}</p>)
                        : null}
                    
                </div>
            </div>
        </>
    )
}

export default Home;