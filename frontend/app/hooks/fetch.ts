export async function clientLoader(){
    const res = await fetch('http://localhost:5000/friends')
    const data = await res.json()
    console.log(data)
    return data
}