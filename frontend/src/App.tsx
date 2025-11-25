import { useState } from "react";
import "./App.css";
import { BACKEND_URL } from "./constants";

export default function App() {
  const [count, setCount] = useState<number>(0);
  const [isSuccess, setIsSuccess] = useState<boolean>(false);
  const [isError, setIsError] = useState<boolean>(false);
  const [isPending, setIsPending] = useState<boolean>(false);

  function increment(): void {
    setCount((prevCount) => prevCount + 1);
  }

  async function fetchServer(): Promise<void> {
    try {
      setIsError(false);
      setIsSuccess(false);
      setIsPending(true);
      const res = await fetch(BACKEND_URL);
      const data = await res.json();

      setIsSuccess(true);
      setIsError(false);
      console.log(data);
    } catch (error) {
      setIsSuccess(false);
      setIsError(true);
      console.warn(error);
    } finally {
      setIsPending(false);
    }
  }

  return (
    <div className="mt-50 grid gap-8">
      <div className="flex gap-4">
        <button onClick={increment}>Count is {count}</button>
        <button onClick={fetchServer}>Fetch server</button>
      </div>
      {isSuccess && <p className="text-green-500">Success</p>}
      {isError && <p className="text-red-500">Error</p>}
      {isPending && <p className="text-blue-500">Loading...</p>}
    </div>
  );
}
