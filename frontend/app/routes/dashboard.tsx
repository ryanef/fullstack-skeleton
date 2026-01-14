
export async function clientLoader(){
    const res = await fetch('http://localhost:5000/friends')
    const friends = await res.json()
    return friends
}
export default function Dashboard({ loaderData }){
    const  users  = loaderData;
    console.log(users)

    const defaultUser = {
        first: "Bob"
    }


    return (
        <>
            <h2>Welcome, {defaultUser.first}</h2>

            <div>
                <h3>Your friends</h3>
                <ul>
                    {users.map((user)=>{
                        return (
                            <li>{user.first}</li>
                        )
                    })}
                </ul>
            </div>
        </>
    )
}